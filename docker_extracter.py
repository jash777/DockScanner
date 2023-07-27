import sys
import docker
from tabulate import tabulate


def pull_image(client, image_url):
    print(f"Pulling Docker image {image_url}...")
    for event in client.api.pull(image_url, stream=True, decode=True):
        if "status" in event:
            print(event["status"])

def extract_packages(client, image_url):
    print("Extracting packages from the Docker image...")

    container = client.containers.create(image_url, command="apk info -v", detach=True)
    container.start()
    container.wait()

    logs = container.logs().decode("utf-8").strip()
    packages = [line.strip() for line in logs.split("\n") if line.strip()]
    container.remove()

    print("Packages extracted successfully!")
    return packages

def display_packages_table(packages):
    headers = ["Name", "Version"]
    rows = [pkg.split() for pkg in packages]
    print(tabulate(rows, headers=headers, tablefmt="grid"))



def main(image_url):
    client = docker.from_env()

    pull_image(client, image_url)
    packages = extract_packages(client, image_url)

    print("\nDocker Image Scan For Vulnerabilities\n")
    display_packages_table(packages)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <docker_image_url>")
        sys.exit(1)

    image_url = sys.argv[1]
    main(image_url)