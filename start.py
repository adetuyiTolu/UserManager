import os,sys,platform,subprocess

print('Welcome to Alc microsoft Advanced Devops Assessment\n')
print('Make Sure you have docker and docker compose installed\n')

# Set Docker Installation status to false
is_docker_installed = False

#Check if docker is installed
try:
    res = subprocess.check_output(["docker", "info"])

    #set docker installation status to true
    is_docker_installed = True
except subprocess.CalledProcessError:
    sys.exit("Make sure your docker is running")
except OSError :
    sys.exit("Docker may not be installed")

#print this error message if docker is not installed
if not is_docker_installed :
    print("Docker Compose not Installed \n kindly install and try again")

app_platform = platform.system()

# execute neccessary command based on platform to setup the application
print('Now setting up your application...\n')

if is_docker_installed:
    if (app_platform == "Linux"):
        os.system("sudo docker-compose build")
        print('Just finished building...')
        os.system("sudo docker-compose up")
    else:
        os.system("docker-compose build")
        print('Just finished building...')
        os.system("docker-compose up")
