use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

pub fn p1() -> u32 {
    let res = read_input();

    return *res.iter().max().unwrap();
}

pub fn p2() -> u32 {
    let mut res = read_input();

    res.sort();
    let s = res.iter().rev().take(3).sum();
    return s;
}

fn read_input() -> Vec<u32> {
    let input = lines_from_file("../input/01.txt").unwrap();

    let mut res: Vec<u32> = Vec::new();
    let mut sum: u32 = 0;
    for l in input {
        if l.trim() == "" {
            res.push(sum);
            sum = 0;
        } else {
            sum += l.parse::<u32>().unwrap();
        }
    }
    res.push(sum);
    return res;
}

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}
