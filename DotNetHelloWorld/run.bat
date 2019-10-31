docker build . -t helloworlddotnet --no-cache
docker run -v %cd%\output:/output helloworlddotnet
