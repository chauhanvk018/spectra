print("Hello folks,post hook implementation is started")

from azure.storage.blob import BlobServiceClient, BlobClient
# Your storage account name and key
account_name = "spectraqastorage"
account_key = "71puuXa1MSNXWYRxfRsQ6Iopyg4IRR48t+AYeb+btsTVppDJri9J/QovUrESagejHvsYHzBmQpEN+AStLSpHRg=="
# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
# Define your container and the blob names
container_name = "democontainer"
source_blob_name = "test/indian cities.csv"  # Example: 'folder/myfile.txt'
archive_blob_name = f"archive/{source_blob_name}"  # Move to archive folder within the same path
# Get the container client
container_client = blob_service_client.get_container_client(container_name)
# Copy the blob to the new location (archive folder)
copied_blob = container_client.get_blob_client(archive_blob_name)
source_blob = container_client.get_blob_client(source_blob_name)
copy_operation = copied_blob.start_copy_from_url(source_blob.url)
# Wait for the copy operation to complete (optional, but recommended for larger files)
copy_operation.wait_for_completion()
# Delete the original blob
container_client.delete_blob(source_blob_name)
print("Hello folks, just now post hook implementation is completed")
