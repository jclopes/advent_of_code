use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

#[derive(Debug)]
struct Monkey {
    items: Vec<u64>,
    op: String,
    arg: u64,
    test: u64,
    exit_true: usize,
    exit_false: usize,
    count: usize,
}

pub fn p1() -> usize {
    let mut input = read_input();

    for _round in 0..20 {
        for m in 0..input.len() {
            let exit_true = input[m].exit_true;
            let exit_false = input[m].exit_false;
            let test = input[m].test;
            let op = &input[m].op;
            let arg = input[m].arg;

            let pis: Vec<u64> = input[m].items.iter()
                .map(|i| process_item(*i, op, arg))
                .rev().collect();
            for i in pis {
                if i % test == 0 {
                    input[exit_true].items.push(i);
                } else {
                    input[exit_false].items.push(i);
                }
            }
            input[m].count += input[m].items.len();
            input[m].items.clear();
        }
    }
    input.sort_by(|a , b| a.count.cmp(&b.count));
    let a = input.pop().unwrap();
    let b = input.pop().unwrap();

    return a.count * b.count;
}

pub fn p2() -> usize {
    let mut input = read_input();
    let mut max_value = 1;
    for m in 0..input.len() {
        max_value *= input[m].test;
    }

    for _round in 0..10000 {
        for m in 0..input.len() {
            let exit_true = input[m].exit_true;
            let exit_false = input[m].exit_false;
            let test = input[m].test;
            let op = &input[m].op;
            let arg = input[m].arg;

            let pis: Vec<u64> = input[m].items.iter()
                .map(|i| process_item_stress(*i, op, arg, max_value))
                .rev().collect();
            for i in pis {
                if i % test == 0 {
                    input[exit_true].items.push(i);
                } else {
                    input[exit_false].items.push(i);
                }
            }
            input[m].count += input[m].items.len();
            input[m].items.clear();
        }
    }
    input.sort_by(|a , b| a.count.cmp(&b.count));
    let a = input.pop().unwrap();
    let b = input.pop().unwrap();

    return a.count * b.count;
}

fn process_item(item: u64, op: &str, arg: u64) -> u64 {
    let mut res = match op {
        "+" => item + arg,
        "-" => item - arg,
        "*" => item * arg,
        "/" => item / arg,
        "^" => item * item,
        _ => item,
    };
    res /= 3;
    return res;
}

fn process_item_stress(item: u64, op: &str, arg: u64, max_value: u64) -> u64 {
    let mut res = match op {
        "+" => item + arg,
        "-" => item - arg,
        "*" => item * arg,
        "/" => item / arg,
        "^" => item * item,
        _ => item,
    };
    res %= max_value;
    return res;
}

fn read_input() -> Vec<Monkey> {
    let input = lines_from_file("../input/11.txt").unwrap();
    let mut res = Vec::<Monkey>::new();
    let mut lines = input.iter();
    loop {
        // Monkey Number - we ignore
        lines.next();

        // Starting items
        let mut l = lines.next();
        let items: Vec<u64> = l.unwrap().trim()
            .trim_start_matches("Starting items:")
            .split(",")
            .map(|x| x.trim().parse::<u64>().unwrap())
            .collect();

        // Operation & Argument
        l = lines.next();
        let op: Vec<&str> = l.unwrap()
            .trim().trim_start_matches("Operation: new = old")
            .trim().split(" ").collect();
        let (m_op, m_arg) = match (op[0], op[1]) {
            ("*", "old") => ("^", 2),
            (o, n) => (o, n.parse::<u64>().unwrap()),
        };

        // Divisible by
        l = lines.next();
        let test = l.unwrap()
            .trim().trim_start_matches("Test: divisible by")
            .trim().parse::<u64>().unwrap();

        // Exit true
        l = lines.next();
        let exit_true = l.unwrap()
            .trim().trim_start_matches("If true: throw to monkey")
            .trim().parse::<usize>().unwrap();

        // Exit false
        l = lines.next();
        let exit_false = l.unwrap()
            .trim().trim_start_matches("If false: throw to monkey")
            .trim().parse::<usize>().unwrap();

        res.push(
            Monkey {
                items: items,
                op: String::from(m_op),
                arg: m_arg,
                test: test,
                exit_true: exit_true,
                exit_false: exit_false,
                count: 0,
            }
        );

        l = lines.next();
        if l == None {
            break;
        }
    }
    return res;
}

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}
