try:
    from robot_drive import RobotDrive
except ImportError:
    from ..robot_drive.robot_drive import RobotDrive
import argparse


if __name__ == "__main__":
    
    rd = RobotDrive()
    
    parser = argparse.ArgumentParser(description="Commands for robot")
    # Manual control
    parser.add_argument("-m", "--manual", action="store_true",
                        help="Activate keyboard control, `--speed` required.")
    
    # Specific actions
    parser.add_argument("-f", "--forward", action="store_true",
                        help="Drive forward, `--speed` required, `-t` or `-d` required.")
    parser.add_argument("-b", "--backward", action="store_true",
                        help="Drive backward, `--speed` required, `-t` or `-d` required.")
    parser.add_argument("-l", "--left", action="store_true",
                        help="Rotate left, `--speed` required, `-t` or `-d` required.")
    parser.add_argument("-r", "--right", action="store_true",
                        help="Rotate right, `--speed` required, `-t` or `-d` required.")
    
    # Supporting arguments
    parser.add_argument("-t", "--time", type=float, metavar="",
                        help="Set time in seconds.")
    parser.add_argument("-s", "--speed", type=int, metavar="",
                        help="Set motor speed between 0 and 255 inclusive.")
    parser.add_argument("-d", "--distance", "--degrees", type=float, metavar="",
                        help="Set driving distance in inches or rotation in degrees.")
    
    args = parser.parse_args()

    if args.manual and args.speed:
        rd.keyboard_control(args.speed)
    elif args.forward or args.backward:
        assert args.speed, "Missing -s arg"
        assert args.time or args.distance, "Need either -t or -s args, use -h to learn more."
        
        # Set positive speed for forward, negative for backward
        speed = args.speed * (-1 if args.backward else 1)
        
        if args.time:
            rd.drive(args.time, speed)
        else:
            rd.drive_distance(args.distance, speed)
    elif args.left or args.right:
        assert args.speed, "Missing -s arg"
        assert args.time or args.distance, "Need either -t or -d args, use -h to learn more."
        
        # Set positive speed for right, negative for left
        speed = args.speed * (-1 if args.left else 1)
        
        if args.time:
            rd.rotate(args.time, speed)
        else:
            rd.rotate_degrees(args.distance, speed)
    else:
        parser.print_help()
