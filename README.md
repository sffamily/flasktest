# flasktest

# local F5

Have Python extension installed. F5 and pick Flask. The test REST API runs at https://localhost:5000 

![API response](img/image.png)

# Code to ACA

Have Azure Container Apps extension installed.
Now from Command Palette to run "Azure Container Apps: Deploy Project from Workspace"
![alt text](img/image-1.png)

Choose proper Azure subscription (It may ask you to sign in Azure first)
create a new or pick existing ACA environment
![alt text](img/image-2.png)

Give it a unique name, then wait until the process done. You will see the status like this:
![alt text](img/image-4.png)

Click blue button and follow the instruction to open the deployed URL on ACA.

Or go to Azure Portal, find the ACA deployed "Application URL"
![alt text](img/image-5.png)

Now fire up browser and run an API <Application URL>/books, it should show:
![alt text](img/image-6.png)

Now it is running in the cloud from ACA!