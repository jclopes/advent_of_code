use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

use std::collections::HashSet;

pub fn p1() -> usize {
    let input = read_input();
    let mut res: HashSet<(i32, i32)> = HashSet::new();
    let mut h: (i32, i32) = (0, 0);
    let mut t: (i32, i32) = (0, 0);

    res.insert(t);

    for (v, s) in input {
        for _i in 0..s {
            h = sum_vector(h, v);
            t = sum_vector(t, move_t(h, t));
            res.insert(t);
        }
    }
    return res.len();
}

pub fn p2() -> usize {
    let input = read_input();
    let mut res: HashSet<(i32, i32)> = HashSet::new();
    let mut h: (i32, i32) = (0, 0);
    let mut h1: (i32, i32) = (0, 0);
    let mut h2: (i32, i32) = (0, 0);
    let mut h3: (i32, i32) = (0, 0);
    let mut h4: (i32, i32) = (0, 0);
    let mut h5: (i32, i32) = (0, 0);
    let mut h6: (i32, i32) = (0, 0);
    let mut h7: (i32, i32) = (0, 0);
    let mut h8: (i32, i32) = (0, 0);
    let mut t: (i32, i32) = (0, 0);

    res.insert(t);

    for (v, s) in input {
        for _i in 0..s {
            h = sum_vector(h, v);
            h1 = sum_vector(h1, move_t(h, h1));
            h2 = sum_vector(h2, move_t(h1, h2));
            h3 = sum_vector(h3, move_t(h2, h3));
            h4 = sum_vector(h4, move_t(h3, h4));
            h5 = sum_vector(h5, move_t(h4, h5));
            h6 = sum_vector(h6, move_t(h5, h6));
            h7 = sum_vector(h7, move_t(h6, h7));
            h8 = sum_vector(h8, move_t(h7, h8));
            t = sum_vector(t, move_t(h8, t));
            res.insert(t);
        }
    }
    return res.len();
}

fn sum_vector(a: (i32, i32), b: (i32, i32)) -> (i32, i32) {
    let (ax, ay) = a;
    let (bx, by) = b;
    (ax + bx, ay + by)
}

fn move_t(h: (i32, i32), t: (i32, i32)) -> (i32, i32 ) {
    let dx = h.0 - t.0;
    let dy = h.1 - t.1;
    match (dx, dy) {
        (2, b) => {
            if b == 0 {
                (1, 0)
            } else {
                (1, b/b.abs())
            }
        },
        (-2, b) => {
            if b == 0 {
                (-1, 0)
            } else {
                (-1, b/b.abs())
            }
        },
        (b, 2) => {
            if b == 0 {
                (0, 1)
            } else {
                (b/b.abs(), 1)
            }
        },
        (b, -2) => {
            if b == 0 {
                (0, -1)
            } else {
                (b/b.abs(), -1)
            }
        },
        _ => (0, 0),
    }
}

fn direction(dir: &str) -> (i32, i32) {
    match dir {
        "U" => (0, 1),
        "D" => (0, -1),
        "L" => (-1, 0),
        "R" => (1, 0),
        _ => (0, 0),
    }
}

fn read_input() -> Vec<((i32, i32), i32)> {
    let input = lines_from_file("../input/09.txt").unwrap();
    input.iter().map(|s| {
        let mut v = s.split(" ");
        (direction(v.next().unwrap()), v.next().unwrap().parse::<i32>().unwrap())
    }).collect()
}

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}
