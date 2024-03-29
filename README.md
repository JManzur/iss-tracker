# Flask ISS Tracker

This is a demo application built using Flask, this demo application demonstrates how to correctly generate healthchecks pages and how to store data in the Docker ephemeral storage. The application makes calls to the [Open Notify ISS Location API](http://api.open-notify.org) to display the current location of the [International Space Station (ISS)](https://www.nasa.gov/mission_pages/station/main/index.html) in real-time.

![App Screenshot](images/iss_tracker.png)

## Functionality

The application has the following functionality:

-   Displays the current location of the ISS on a web page.
-   Allows users to switch between light and dark mode using a toggle button.
-   Saves the response from the ISS API in a local log file (`aiss-now.log`) every time the page is refreshed.
-   Provides a `/status` endpoint that returns a health check status based on whether the ISS API is available or not.

## Technologies Used

The following technologies were used to build this application:

-   [Python](https://www.python.org/) - A high-level programming language used to build the Flask application.
-   [Flask](https://flask.palletsprojects.com/en/2.1.x/) - A lightweight web framework used to build the application.
-   [Urllib3](https://urllib3.readthedocs.io/en/latest/) - A powerful HTTP client library used to make API requests to the ISS API.
-   [jQuery](https://jquery.com/) - A JavaScript library used to add interactivity to the web page.
-   [Docker](https://www.docker.com/) - A containerization platform used to package and deploy the application.

## Usage

You can run the application using either plain Docker or Docker-Compose. Follow the steps below:

Using plain Docker:
- Clone the repository to your local machine:
  - `git clone https://github.com/JManzur/iss-tracker.git`
- Navigate to the cloned repository and build the Docker container:
  - `cd iss-tracker`
  - `docker build -t iss-tracker .`
- Run the Docker container:
  - `docker run -p 5002:5002 --name iss-tracker iss-tracker`
- You can then access the application by visiting `http://localhost:5002` in your web browser.


Using Docker-Compose:
- Clone the repository to your local machine:
  - `git clone https://github.com/JManzur/iss-tracker.git`
- Navigate to the cloned repository and run the Docker container:
  - `cd iss-tracker`
  - `docker-compose up -d`
- You can then access the application by visiting `http://localhost:5002` in your web browser.