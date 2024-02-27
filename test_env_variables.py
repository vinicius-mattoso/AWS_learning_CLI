# Import libs
import os
from dotenv import load_dotenv

# Load the .env
load_dotenv()

# Get AWS credentials and region from environment variables
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

# Print the variables:

print(f'''AWS_ACCESS: {aws_access_key_id} \n
AWS_SECRET: {aws_secret_access_key}''')