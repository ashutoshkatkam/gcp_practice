from google.cloud import run_v2

def oveeride_sample_run_job(timeout_seconds):
    # Create a client
    client = run_v2.JobsClient()

    # Initialize request argument(s)
    request = run_v2.RunJobRequest(
        name="overrides_sample_job",
        overrides = {
    "env_vars": [{"name": "ENV_1", "value": "Beta-1"}],
    "command": ["python", "version1.py", "--filename", "image_1.jpeg"],
    "task_timeout": str(timeout_seconds) + "s"
    }
    )

    # Make the request
    operation = client.run_job(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# import google.cloud.run_v2 as run_v2

# # Replace with your specific values
# service_name = "your-service-name"
# image_url = "gcr.io/your-project/your-image:latest"

# def create_job_with_timeout_override(timeout_seconds):
#     client = run_v2.ServicesClient()
#     job = {
#         "name": service_name,
#         "image_url": image_url,
#         "overrides": {
#             "task_timeout": str(timeout_seconds) + "s"  # Specify timeout in seconds
#         }
#     }
#     try:
#         response = client.run_service(request={"job": job})
#         print(f"Job created with name: {response.name}")
#     except GoogleAPIError as e:
#         print(f"Error creating job: {e}")

# # Example usage:
# create_job_with_timeout_override(3600)  # Set timeout to 1 hour
