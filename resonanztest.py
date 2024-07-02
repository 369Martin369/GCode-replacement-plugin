def generate_resonance_gcode(output_file_path, initial_feedrate=3000, max_feedrate=8000, step=100):
    start_script = """;TARGET_MACHINE.NAME:BLV mgn Cube350
T0
M82 ;absolute extrusion mode
G21 ;metric values
G90 ;absolute positioning
M107 ;start with the fan off
G92 E0 ;zero the extruded length
G32

;LAYER:0
M107
M204 P1000 T1000 ;Set printing and travel accelerations
M566 X600 Y600 ;Set allowable instantaneous speed change mm/min
;-----Startscript-End------
"""

    x_start = 50
    y_start = 50
    square_size = 200
    
    with open(output_file_path, 'w') as file:
        # Write the start script
        file.write(start_script)
        
        # Initial position
        file.write(f"G0 X{x_start} Y{y_start} F{initial_feedrate}\n")
        
        feedrate = initial_feedrate
        while feedrate <= max_feedrate:
            file.write(f"; Current feedrate: {feedrate}\n")  # Comment to output the current feedrate
            file.write(f"M117 Feedrate: {feedrate}\n")  # Display the current feedrate on the printer's LCD
            
            # Move to each corner of the square
            file.write(f"G1 X{x_start + square_size} Y{y_start} F{feedrate}\n")
            file.write(f"G1 X{x_start + square_size} Y{y_start + square_size} F{feedrate}\n")
            file.write(f"G1 X{x_start} Y{y_start + square_size} F{feedrate}\n")
            file.write(f"G1 X{x_start} Y{y_start} F{feedrate}\n")
            
            # Increase the feedrate for the next layer
            feedrate += step

        # Move back to the starting point at the maximum feedrate
        file.write(f"G0 X50 Y50 F{max_feedrate}\n")

if __name__ == "__main__":
    output_file = 'resonance_test.gcode'
    generate_resonance_gcode(output_file)
    print(f"Resonance test G-code saved to {output_file}")
