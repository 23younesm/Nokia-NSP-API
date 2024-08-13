# Nokia-NSP-API

A simple API interaction scirpt to push and pull data from a Nokia NSP appliance. This program was built during my summer internship with FirstEnergy.

## Installation

To install the project, follow these steps:

```
$ git clone https://github.com/23younesm/Nokia-NSP-API.git
$ cd project
```

## Usage

To use the project, adjust the varibles (Server IP and Token) and then run the following command:

```
$ python3 api.py
```

Every 30 mins, Nokia needs a new authorization token for the API to validate. To refresh the token run the following command when needed:

```
$ python3 refresh.py
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make changes and commit them
4. Push to the branch (`git push origin feature-branch`)
5. Create a pull request

## License

This project is licensed under the [MIT License](LICENSE).
