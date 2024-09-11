# DWDM-Network-Optimization-Tool
## Overview

The **Network DWDM Optimizer** is a comprehensive tool designed to optimize Dense Wavelength Division Multiplexing (DWDM) networks. This application integrates various functionalities to provide real-time network status, manage network paths, and optimize network performance.

## Features

- **Real-time Network Status:** Monitor the status of the network in real-time using WebSocket connections.
- **Dynamic Path Management:** Manage and optimize network paths, including source, destination, wavelength, and latency.
- **Redis Integration:** Use Redis for caching and real-time updates.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**: For running the application and dependencies.
- **Redis**: For caching and real-time data management.
- **Django**: The web framework used in this project.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/dwdm_network_optimizer.git
   cd dwdm_network_optimizer
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Redis**

   Download and extract Redis if you haven't already:
   * **For Windows**: Download Redis from [Redis for Windows](https://github.com/tporadowski/redis/releases) and extract it.
   * **For Linux/Mac**: Use package managers or build from source.

   Start Redis server on port 6380:

   ```bash
   redis-server.exe --port 6380
   ```

5. **Configure Django Settings**

   Update the `settings.py` file with the correct Redis port:

   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.redis.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6380/1',
       }
   }
   ```

6. **Run Database Migrations**

   ```bash
   python manage.py migrate
   ```

7. **Start the Django Development Server**

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000`.
7. **Output**
![screen](https://github.com/user-attachments/assets/6873092f-0d5c-4637-9058-99048e113fd7)

## WebSocket Configuration

The application uses WebSockets for real-time updates. Ensure the WebSocket server is properly configured to connect with the Redis server on port 6380.

## Troubleshooting

- **Redis Connection Issues**: Ensure Redis is running on the correct port (6380) and is accessible. Check the Redis logs for any errors.
- **Port Permission Issues**: If you encounter permission errors when starting the Django server, ensure no other application is using the same port.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. For any issues or feature requests, open an issue in the GitHub repository.

## Contact

For questions or feedback, please reach out to akstiwari307@gmail.com.

