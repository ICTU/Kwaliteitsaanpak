FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /app

# install System.Drawing native dependencies
RUN apt-get update \
    && apt-get install -y --allow-unauthenticated \
        libc6-dev \
        libgdiplus \
        libx11-dev \
     && rm -rf /var/lib/apt/lists/* \
     && ls /usr/lib/x86_64-linux-gnu

# copy csproj and restore as distinct layers
COPY *.csproj ./dotnetapp/
WORKDIR /app/dotnetapp
RUN dotnet restore

# copy and publish app and libraries
WORKDIR /app/
COPY *.cs ./dotnetapp/
WORKDIR /app/dotnetapp
RUN dotnet publish -c Release /p:PublishingSingleFile=true -o /app/out

FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS runtime
WORKDIR /app/out
COPY --from=build /app/out ./
RUN ls -la
RUN chmod +x mdconvert
ENTRYPOINT ["./mdconvert"]