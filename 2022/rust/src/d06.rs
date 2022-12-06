use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

pub fn p1() -> u32 {
    let input = read_input();

    return find_marker(&input, 4);
}

pub fn p2() -> u32 {
    let input = read_input();

    return find_marker(&input, 14);
}

fn find_marker(input: &String, size: usize) -> u32 {
    let mut p = 0;
    let mut window = Vec::new();
    for c in input.chars() {
        window.push(c);
        if window.len() > size {
            window.remove(0);
        }
        p += 1;
        if window.len() < size { continue; }
        if is_marker(&window, size) {
            break;
        }
    }
    return p;
}

fn is_marker(input: &Vec<char>, size: usize) -> bool {
    for i in 0..(size - 1) {
        for j in (i + 1)..size {
            if input[i] == input[j] {
                return false;
            }
        }
    }
    return true;
}

fn read_input() -> String {
    let mut input = lines_from_file("../input/06.txt").unwrap();
    return input.pop().unwrap();
}

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}
