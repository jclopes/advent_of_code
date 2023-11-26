use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

#[derive(Debug)]
struct Status {
    pwd: Vec<String>,
    pc: usize,
}

pub fn p1() -> u32 {
    let input = read_input();
    let mut staus = Status {
        pwd: vec![String::from("/")],
        pc: 0,
    };

    let mut parent: HashMap<String, String> = HashMap::new();
    let mut children: HashMap<String, Vec<String>> = HashMap::new();
    let mut size: HashMap<String, u64> = HashMap::new();

    return 0;
}

pub fn p2() -> u32 {
    let input = read_input();

    return 0;
}

fn parse_cmd(arg: Type) -> RetType {
    unimplemented!();
}

fn read_input() -> String {
    return input = lines_from_file("../input/07.txt").unwrap();
}

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}
