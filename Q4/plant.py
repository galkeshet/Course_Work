import argparse
import matplotlib.pyplot as plt
import os

def plot_plant_growth(plant, height, leaf_count, dry_weight, output_dir):
    plt.figure(figsize=(10, 5))

    # Height Plot
    plt.subplot(3, 1, 1)
    plt.plot(height, marker='o', label='Height')
    plt.ylabel("Height (cm)")
    plt.title(f"{plant} Growth Data")
    plt.legend()

    # Leaf Count Plot
    plt.subplot(3, 1, 2)
    plt.plot(leaf_count, marker='s', color='g', label='Leaf Count')
    plt.ylabel("Leaf Count")
    plt.legend()

    # Dry Weight Plot
    plt.subplot(3, 1, 3)
    plt.plot(dry_weight, marker='^', color='r', label='Dry Weight')
    plt.ylabel("Weight (g)")
    plt.xlabel("Time Steps")
    plt.legend()

    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{plant}_growth.png")
    plt.savefig(output_path)
    print(f"Saved plot: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plant Growth Data Visualization")

    parser.add_argument("--plant", type=str, required=True, help="Plant Name")
    parser.add_argument("--height", type=float, nargs="+", required=True, help="Plant height values")
    parser.add_argument("--leaf_count", type=int, nargs="+", required=True, help="Leaf count values")
    parser.add_argument("--dry_weight", type=float, nargs="+", required=True, help="Dry weight values")
    parser.add_argument("--output_dir", type=str, default="./", help="Directory to save the plots")

    args = parser.parse_args()
    
    os.makedirs(args.output_dir, exist_ok=True)
    plot_plant_growth(args.plant, args.height, args.leaf_count, args.dry_weight, args.output_dir)
