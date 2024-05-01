"custom/todo": {
    "exec": "python $HOME/.config/waybar/modules/todo.py",
    "on-click": "kitty -e nvim $HOME/.config/waybar/modules/todo.txt",
    "format": "  {} ",
    "return-type": "json",
    "tooltip": true,
    "interval": 5
