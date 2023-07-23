#!/bin/bash
echo "[LOG] 01. local deploy.."
IMAGE_NAME=demoapp
IMAGE_VERSION=1.0
TARGET_PORT=9000
#echo ${IMAGE_NAME}:${IMAGE_VERSION}


echo "[LOG] 02. container cleansing.."
docker stop `docker ps | grep -e "${IMAGE_NAME}:${IMAGE_VERSION}" | awk '{print $1}'`
docker rmi -f ${IMG_NAMME}:${IMAGE_VERSION}

echo "[LOG] 03. image build.."
docker build -t ${IMAGE_NAME}:${IMAGE_VERSION} .

echo "[LOG] 04. container run.."
docker run -p ${TARGET_PORT}:${TARGET_PORT} -d ${IMAGE_NAME}:${IMAGE_VERSION}

docker ps | grep -e ${IMAGE_NAME}