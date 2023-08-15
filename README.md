<a name="readme-top"></a>

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/numpy)


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ConfusedCharacter/Prypto">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Prypto</h3>

  <p align="center">
    Welcome to Prypto - Picture Cryptography Tool!
    <br />
    <br />
    ·
    <a href="https://github.com/ConfusedCharacter/Prypto/issues">Report Bug</a>
    ·
    <a href="https://github.com/ConfusedCharacter/Prypto/issues">Request Feature</a>
  </p>
</div>


## About The Prypto

Prypto is an open-source tool designed to convert files into photos and vice versa. It allows you to encrypt files by converting them to images and decrypt them back to files. By adding a password to your files, Prypto uses AES encryption to ensure their security.



### Here's how it works:


* 1. File Conversion: Prypto utilizes the RGB range of 0 to 255 in images. To convert a file into a picture, the tool first encodes the file into Base64 format. Base64 characters range up to 128, so each character is further converted into decimal using the 'ord' function. Each pixel of the image is then used to store the decimal value of a character.

* 2. Encryption: When decrypting the picture back into a file, Prypto reverses the process. It reads the pixel values from the image and converts them back to decimals. These decimal values are then converted into Base64 characters, and finally, the original file is reconstructed.


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Can be password protected
- [x] Encrypt With AES
- [x] Support all file types for encryption
- [x] The photo is legible and does not break

See the [open issues](https://github.com/ConfusedCharacter/Prypto/issues) for a full list of proposed features (and known issues).


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

ConfusedCharacter - ConfusedCharacterSup@gmail.com

Project Link: [https://github.com/ConfusedCharacter/Prypto](https://github.com/ConfusedCharacter/Prypto)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<p align="right">(<a href="#readme-top">back to top</a>)</p>


