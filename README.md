
# BuyBot

## Table of Contents

1. [Introduction](#introduction)
2. [Background](#background)
3. [Installation](#installation)
4. [Features](#features)
5. [Usage](#usage)
6. [Folder Structure](#folder-structure)
7. [License](#license)

## Introduction

Buybot is a python based automation program designed to secure high demand, limited stock items such as GPUs, gaming consoles, and collectible Pokemon Card Packs at a reasonable price. BuyBot monitors product availability and can automatically complete the checkout process in less than five seconds.

## Background

Buybot was built in response to the increasing number of scalper bots that instantly purchase in demand items, making manual purchasing nearly impossible for consumers. Buybot was built with modularity in mind and supports multiple popular store fronts including Best Buy, Newegg, Amazon, Gamestop, and Microcenter.

## Installation

To run buybot

1. In a command line  the install dependencies by typing 
<br>pip install -r requirements.txt
2. Navigate to the desired product page (e.g. GPU, console, Pokémon card), copy the URL, and paste it into productLinks.txt.
<br>Each link should be on a separate line
<br>Make sure the link matches a supported store (e.g. Amazon, Best Buy, Newegg)
3. Add in any necessary additional checkout information in botConfig.py to allow the bot to complete purchases successfully
<br>Newegg requires cvv
<br>Amazon requires prime status
<br>All stores require whether you want to continuously monitor for availibility or not  
4. Execute buybot.py by typing
<br> python buybot.py

## Features 

* Automated Checkout
* Product availability monitoring
* Retrieval of a list of products given a price and availibility
* Modularity to support additional buybot store additions
* Parallel monitoring and purchasing of products

## Usage

In order to run BuyBot it is recommended to have have
* Python v3.1+
* selenium v4.34.2+
* pandas v2.3.2+
* beautifulsoup4 v4.13.4


## Folder Structure

The stores folder contains the code for the respective storefront buybots
<br><br> botConfig.py contains additional bot settings to modify the buybot as well as paths that allow the bot to navigate through checkout process
<br><br> buyBot.py contains the main buybot program that identifies which store bot to launch
<br> <br> productLinks.txt contains the links to the products that the user wishes to buy
<br> <br> requirements.txt is a helper file that helps automate the environment setup process

## License
This tool is intended for personal use only. Please respect store policies and avoid misuse or resale automation<br>

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.



