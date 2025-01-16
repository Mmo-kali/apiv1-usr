# apiv1-usr
ftc 5202 (NOT SURE IF ILL INCLUDE THE SOURCE CODE FOR THE API)
_________

# API Challenge README

## Overview

This API is designed for a Capture The Flag (CTF) challenge, providing a set of functionalities to interact with user data stored in CSV format. It supports operations to retrieve specific files or data based on given parameters.

## Features

- **File Retrieval**: GET requests allow for the retrieval of specific files from the server, given a valid file name.
- **Data Querying**: POST requests enable querying specific data from a CSV file, based on a given region ID.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install flask`.
3. Start the server with `python api.py`. The API will be available at `http://localhost:8000`.

## API Endpoints

### GET `/apiV1-usr`

Retrieves files from the server.

**Parameters:**

- `debugPin` (optional): A debug pin for testing purposes.
- `fileName`: The name of the file to retrieve. Use `*` to list all available files.

**Responses:**

- `200 OK`: File or file list successfully retrieved.
- `400 Bad Request`: Required parameters are missing.
- `403 Forbidden`: Invalid request due to incorrect `debugPin`.
- `404 Not Found`: The specified file was not found.

### POST `/apiV1-usr`

Queries data from a CSV file based on the provided region ID.

**Body:**

- `RegionID`: The ID of the region to query.

**Responses:**

- `200 OK`: Data successfully retrieved.
- `404 Not Found`: The specified region ID was not found.

## Error and Debugging

In case of encountering errors, the API provides descriptive error messages to assist in debugging. For testing and debugging purposes, a default `debugPin` is provided: `335-818-834`. This pin should be used cautiously and only in a secure testing environment to prevent unintended data exposure.

## Security Considerations

Ensure that the API is not exposed to the public internet without proper security measures in place, especially when using the `debugPin` feature.

## Documentation

For further details on request formats and additional parameters, refer to the API source-code.

## Support

For support or to report issues, please file an issue on the GitHub repository associated with this challenge.
