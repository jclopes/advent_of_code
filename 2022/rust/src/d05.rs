// [N]     [C]                 [Q]    
// [W]     [J] [L]             [J] [V]
// [F]     [N] [D]     [L]     [S] [W]
// [R] [S] [F] [G]     [R]     [V] [Z]
// [Z] [G] [Q] [C]     [W] [C] [F] [G]
// [S] [Q] [V] [P] [S] [F] [D] [R] [S]
// [M] [P] [R] [Z] [P] [D] [N] [N] [M]
// [D] [W] [W] [F] [T] [H] [Z] [W] [R]
//  1   2   3   4   5   6   7   8   9 

use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

pub fn p1() -> String {
    let mut stacks = init_state();
    let input = read_input();
    for l in input {
        for _ in 0..l[0] {
            let t = stacks[l[1] - 1].pop().unwrap();
            stacks[l[2] - 1].push(t);
        }
    }
    return top_of_stacks(stacks);
}

pub fn p2() -> String {
    let mut stacks = init_state();
    let input = read_input();
    for l in input {
        let mut t: Vec<&str> = Vec::new();
        for _ in 0..l[0] {
            t.push(stacks[l[1] - 1].pop().unwrap());
        }
        t.reverse();
        stacks[l[2] - 1].append(&mut t);
    }
    return top_of_stacks(stacks);
}

fn top_of_stacks(stacks: Vec<Vec<&'static str>>) -> String {
    let mut res = String::new();
    for i in stacks {
        res.push_str(i.last().unwrap());
    }
    return res;
}

fn init_state() -> Vec<Vec<&'static str>> {
    let mut s1 = vec!["N", "W", "F", "R", "Z", "S", "M", "D"];
    let mut s2 = vec!["S", "G", "Q", "P", "W"];
    let mut s3 = vec!["C", "J", "N", "F", "Q", "V", "R", "W"];
    let mut s4 = vec!["L", "D", "G", "C", "P", "Z", "F"];
    let mut s5 = vec!["S", "P", "T"];
    let mut s6 = vec!["L", "R", "W", "F", "D", "H"];
    let mut s7 = vec!["C", "D", "N", "Z"];
    let mut s8 = vec!["Q", "J", "S", "V", "F", "R", "N", "W"];
    let mut s9 = vec!["V", "W", "Z", "G", "S", "M", "R"];
    s1.reverse();
    s2.reverse();
    s3.reverse();
    s4.reverse();
    s5.reverse();
    s6.reverse();
    s7.reverse();
    s8.reverse();
    s9.reverse();
    vec![s1, s2, s3, s4, s5, s6, s7, s8, s9]
}

fn read_input() -> Vec<Vec<usize>> {
    let input = lines_from_file("../input/05.txt").unwrap();

    let mut res: Vec<Vec<usize>> = Vec::new();
    for l in input {
        if l.is_empty() || l.chars().next().unwrap() != 'm' {
            continue;
        }
        let mut t: Vec<&str> = l.split(' ').collect();
        t.remove(0);
        t.remove(1);
        t.remove(2);
        res.push(t.into_iter().map(|x| x.parse::<usize>().unwrap()).collect());
    }
    return res;
}

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}
