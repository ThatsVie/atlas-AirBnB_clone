# Atlas AirBnB Clone
**Project Description**

This project implements the HBnB console, a command-line interface for managing instances of various classes. The classes are defined in the models folder, and the console allows users to interact with instances of classes such as BaseModel, User, State, City, Place, Amenity, and Review. The console provides functionalities like creating, showing, destroying, updating, and listing instances, among others.

## Models
The models folder contains the following class definitions:

**BaseModel (base_model.py)**

The BaseModel class serves as the base class for other classes. It includes attributes such as id, created_at, and updated_at. The class provides methods for string representation, saving instances, and converting instances to dictionaries.

**Amenity (amenity.py)**

The Amenity class, derived from BaseModel, represents an amenity. It includes a name attribute.

**City (city.py)**

The City class, derived from BaseModel, represents a city. It includes attributes such as state_id and name.

**Place (place.py)**

The Place class, derived from BaseModel, represents a place. It includes attributes such as city_id, user_id, name, description, and others.

**Review (review.py)**

The Review class, derived from BaseModel, represents a review. It includes attributes such as place_id, user_id, and text.

**State (state.py)**

The State class, derived from BaseModel, represents a state. It includes a name attribute.

**User (user.py)**

The User class, derived from BaseModel, represents a user. It includes attributes such as email, password, first_name, and last_name.

## Command Interpreter (console.py)

The command interpreter allows users to interact with the instances of the defined classes. Supported commands include creating, showing, destroying, updating, listing, and counting instances. The console provides a flexible and straight forward way to manage the data.

## Storage (engine/file_storage.py)

The FileStorage class in the engine folder provides an abstracted storage engine. It allows for serialization and deserialization of instances to and from a JSON file (file.json). The FileStorage class is utilized by the console to save and reload instances.


## How to Start

To start the HBnB console, run the console.py script using Python:

![image](https://github.com/ThatsVie/atlas-AirBnB_clone/assets/143755961/7335c65a-b7b3-416c-8605-f5573c74af9c)

## How to Use

Once the console is running, you can use it interactively or in non-interactive mode. Below are examples of both modes:

**Interactive Mode**

![image](https://github.com/ThatsVie/atlas-AirBnB_clone/assets/143755961/338f551f-e7d0-42a2-9396-62d9b1e087d3)


**Non-Interactive Mode**

![image](https://github.com/ThatsVie/atlas-AirBnB_clone/assets/143755961/68003a63-62f9-4b24-99b4-ae8dd43e9ff6)


