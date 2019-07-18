param(
    [Parameter(Mandatory)]
    [string]
    $Base
)

docker build --rm --build-arg BASE="$Base" -f "./Dockerfile" -t "nimashoghi/$($Base.Replace(":", "-").Replace("/", "-"))-orb-slam2-runtime-deps:latest" "./"
docker push "nimashoghi/$Base-orb-slam2-runtime-deps:latest"
