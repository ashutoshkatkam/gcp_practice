from google.cloud import run_v2

def overide_sample_run_job(timeout_seconds):
    # Create a client
    client = run_v2.JobsClient()

    # Initialize request argument(s)
    request = run_v2.RunJobRequest(
        name="projects/user-mcytqvjmikuk/locations/us-central1/jobs/overrides-v1",
        overrides = {"container_overrides":[{"args": ["version1.py", "image_1.jpeg"],"env": [{"name": "ENV_1", "value": "Beta-1"}],"clear_args":False}],
                    "timeout": str(timeout_seconds) + "s",
                    "task_count" : 1
    }
    )

    # Make the request
    operation = client.run_job(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

overide_sample_run_job(100)

