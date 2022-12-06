use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

pub fn p1() -> u32 {
    let input = read_input();
    let mut res = 0;
    for l in input {
        let ids = parse_line(&l);
        if is_total_overlap(ids) {
            res += 1;
        }
    }

    return res;
}

pub fn p2() -> u32 {
    let input = read_input();
    let mut res = 0;
    for l in input {
        let ids = parse_line(&l);
        if is_overlap(ids) {
            res += 1;
        }
    }

    return res;
}

fn is_overlap(ids: [u32; 4]) -> bool {
    let mut res = true;
    if ids[0] > ids[3] {
        res = false;
    }
    if ids[1] < ids[2] {
        res = false;
    }
    return res;
}

fn is_total_overlap(ids: [u32; 4]) -> bool {
    let mut res = true;
    if ids[0] > ids[2] && ids[1] > ids[3] {
        res = false;
    }
    if ids[0] < ids[2] && ids[1] < ids[3] {
        res = false;
    }
    return res;
}

fn parse_line(line: &str) -> [u32; 4] {
    let l = line.replace(',', "-");
    let mut tokens = l.split('-');
    let mut ids: [u32; 4] = [0; 4];
    for i in 0..4 {
        ids[i] = tokens
            .next().expect("Invalid input!")
            .parse().unwrap();
    }
    return ids;
}

fn read_input() -> Vec<String> {
    return lines_from_file("../input/04.txt").unwrap();
}

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}
