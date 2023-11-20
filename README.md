# Rock Paper Scissor

## A rock-paper-scissor game built with tkinter in python.

## Points to take care(since container opens a gui):

1. Install an X server on your host machine (if it's not already installed). On Linux, you can use X.Org, which is the most common X server implementation. On Windows or macOS, you can use Xming or XQuartz, respectively.

2. Open a terminal on your host machine and run the following command to allow connections from any IP address:
   ```bash
   xhost +
   ```

## **Docker-Compse Workflow**

```bash
1. docker-compose up // to build and start the containers
2. docker-compose stop // to stop the containers
3. docker-compose start // to restart the containers
4. docker-compose down // to stop and remove the containers
5. docker-compose up --build // to force build and start the containers
```

## **Docker setup for production and development**

1. docker-compose -f docker-compose.dev.yml up
2. docker-compose -f docker-compose.prod.yml up
