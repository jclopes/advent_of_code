use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

pub fn p1() -> u32 {
    let input = read_input();

    let mut index_l: [u8; 52];
    let mut index_r: [u8; 52];
    let mut score_sum = 0;
    for line in input {
        let mid = line.len() / 2;
        index_l = line_index(&line[..mid]);
        index_r = line_index(&line[mid..]);
        score_sum += line_score(index_l, index_r);
    }
    return score_sum;
}

pub fn p2() -> u32 {
    let mut score_sum = 0;
    let mut index_a: [u8; 52];
    let mut index_b: [u8; 52];
    let mut index_c: [u8; 52];

    let mut input = read_input();
    while input.len() > 0 {
        let mut group = input.drain(..3);
        index_a = line_index(&group.next().unwrap());
        index_b = line_index(&group.next().unwrap());
        index_c = line_index(&group.next().unwrap());
        score_sum += group_score(index_a, index_b, index_c);
    }

    return score_sum;
}

fn line_index(line: &str) -> [u8; 52] {
    let mut index: [u8; 52] = [0; 52];
    let bytes = line.as_bytes();
    for i in bytes {
        let mut li = *i;
        if li > b'Z' {
            li -= b'a';
        } else {
            li -= b'A';
            li += 26;
        }
        index[li as usize] += 1;
    }
    return index;
}

fn line_score(index_l: [u8; 52], index_r: [u8; 52]) -> u32 {
    let mut score: u32 = 0;
    for i in 0..52 {
        if index_l[i] > 0 && index_r[i] > 0 {
            score += i as u32 + 1;
        }
    }
    return score;
}

fn group_score(index_a: [u8; 52], index_b: [u8; 52], index_c: [u8; 52]) -> u32 {
    let mut score: u32 = 0;
    for i in 0..52 {
        if index_a[i] > 0 && index_b[i] > 0 && index_c[i] > 0 {
            score += i as u32 + 1;
        }
    }
    return score;
}

fn read_input() -> Vec<String> {
    return lines_from_file("../input/03.txt").unwrap();
}

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}
