# Typing Trainer

This is a program for training typing that I created using the pygame python library. I develop game modes that help me train my problematic keys, and explore diferent metrics to understand better how I'm performing.

### Installation
To use it, clone this repository and install the required python3 libraries with
`pip install -r requirements.txt`

### Game Modes

#### Uniform
  Selects words uniformly at random to form your text.
#### Weighted
  Selects a letter and forms the text with words containing that letter. It choses the letter following a distribution related to how well the player is performing on that letter, so that problematic keys appear more often than others.
#### Reduced
  Selects words that contains on of the following letters "bcdjkqtvxz". Those were the letter that I'm the slowest on typing.
#### Digits
  Select random digits sequences to form the text.

### Controls
- Main Menu
  - \` (back quote) - Show player stats
  - Arrow keys - Select game mode
  - Enter - Enter training session
- Training session
  - ESC - Return to main menu
  - letters and digits - Input the letter to complete the text
- Stats page
  - ESC - Return to main menu
  
