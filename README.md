# Simple Python Script for Sending Personalized Emails via "mailto:"

This Python script is designed to speed up the process of sending personalized emails, functioning similarly to a basic mail merge. It works smoothly on macOS and requires nothing more than a working version of Python—no additional software is necessary.

## How It Works
The script gathers all the necessary information to generate a "mailto:" URL, then automatically opens your preferred email client’s compose window with the relevant details filled in.

It was born out of frustration with macOS's lack of a native equivalent to Microsoft’s mail merge functionality, and the limitations of the Microsoft suite on macOS (e.g., inability to add CC addresses in mail merges).

## Usage
Just run mailmerge.py in your favorite way.

## Features

- Reads a CSV file containing email addresses and recipient names.
- Reads a text file that serves as the body of the email.
- Opens a new email window in your default email client with the fields pre-filled for review. You can manually press "Send" after checking, or you can choose not to send the email and simply move on to the next recipient.
- After reviewing or editing, press "Enter" to move on to the next recipient.

## What It Doesn’t Do

- It does not automatically send the email. This is intentional, as I prefer to manually review each email before sending (plus, I wanted to avoid the complexities of OAuth just for this simple task).
- There can be issues with special characters like umlauts (e.g., ü, ö, é). These can be resolved by using `urllib.parse` to handle URL encoding.

That’s it! Simple and effective for personalizing emails without too much overhead.
