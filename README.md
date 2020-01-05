# MultiCopy
it gives the user, the possibility to copy 5 things to the clipboard at the same time, then select the copy number and paste it

# how to use
* it catches 'ctrl+c+number' (while number between 0 and 9) and copies the value from the clipboard and stores it in the number'th
  local value

* and to paste, you have to select the position of the values. i.e, if you copied the value from the clipboard using 'ctrl+c+2',
  then, when pastin it, you do 'ctrl+alt+2' and then 'ctrl+v'
  
# Requirements
  * Keyboard module: to monitor keyboard events
  ```
  pip install keyboard
  ```
  * pyperclip module: to copy and paste from the clipboard
  ```
  pip install pyperclip
  ```
