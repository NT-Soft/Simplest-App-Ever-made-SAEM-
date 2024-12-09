def draw_ascii_window(title, width, height):
    if len(title) > width - 4:
        title = title[:width - 4] + "..."
    
    # Top border with title
    print("+" + "-" * (width - 2) + "+")
    print("| " + title.ljust(width - 4) + " |")
    
    # Empty content area
    for _ in range(height - 3):
        print("|" + " " * (width - 2) + "|")
    
    # Bottom border
    print("+" + "-" * (width - 2) + "+")
draw_ascii_window("My ASCII Window", 30, 10)