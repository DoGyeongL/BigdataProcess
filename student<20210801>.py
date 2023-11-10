import sys

def count_movies_by_genre(input_file, output_file):
    genre_count = {}

    with open(input_file, 'r', encoding='latin-1') as file:
        for line in file:
            _, _, genres = line.strip().split('::')
            movie_genres = genres.split('|')

            for genre in movie_genres:
                if genre in genre_count:
                    genre_count[genre] += 1
                else:
                    genre_count[genre] = 1

    with open(output_file, 'w') as output:
        for genre, count in genre_count.items():
            output.write(f"{genre} {count}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 IMDBStudent<20210801>.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    count_movies_by_genre(input_file, output_file)
    print(output_file)
