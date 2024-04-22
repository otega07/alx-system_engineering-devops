# Manifest to install Flask (2.1.0) from pip3

# Define a class for managing Flask installation
class mymodule::flask_install {
    package { 'flask':
        ensure   => '2.1.0',
        provider => 'pip3',
    }
}

# Define main manifest
class { 'mymodule::flask_install': }
