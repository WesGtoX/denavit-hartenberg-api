<h1 align="center">
  Denavit-Hartenberg API
  <br />
</h1>

<p align="center">
  <a href="#about-the-project">About</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#technology">Technology</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#getting-started">Getting Started</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#roadmap">Roadmap</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#how-to-contribute">Contributing</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

<p align="center">
  <img alt="Denavit-Hartenberg API CI" src="https://github.com/WesGtoX/denavit-hartenberg-api/actions/workflows/fastapi-app.yml/badge.svg" />
  <img alt="codecov" src="https://codecov.io/gh/WesGtoX/denavit-hartenberg-api/branch/main/graph/badge.svg?token=CXVI4FZPTM" />
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/wesgtox/denavit-hartenberg-api?style=plastic" />
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/wesgtox/denavit-hartenberg-api?style=plastic" />
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/wesgtox/denavit-hartenberg-api?style=plastic" />
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/wesgtox/denavit-hartenberg-api?style=plastic" />
  <img alt="License" src="https://img.shields.io/github/license/wesgtox/denavit-hartenberg-api?style=plastic" />
</p>


## About the Project

API to determine the position of a robot's claw using the Denavit-Hartenberg model.


## Technology

This project was developed with the following technologies:

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)


## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)


### Install and Run

1. Clone the repository:
```bash
git clone https://github.com/WesGtoX/denavit-hartenberg-api.git
```
2. Install the dependencies:
```bash
poetry install
```
3. Run:
```bash
poetry run uvicorn app.main:app --reload
```


## Roadmap

See the [open issues](https://github.com/WesGtoX/denavit-hartenberg-api/issues) for a list of proposed features (and known issues).


## How to contribute

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch `git checkout -b feat/my-feature`.
3. Commit your Changes `git commit -m 'feat: My new feature'`.
4. Push to the Branch `git push origin feat/my-feature`.
5. Open a Pull Request.

After the merge of your pull request is done, you can delete your branch.


## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

Made with ♥ by [Wesley Mendes](https://wesleymendes.com.br/) :wave:
