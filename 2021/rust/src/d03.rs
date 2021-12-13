use std::{
    io::{self, Read},
};

const MASK: [u32; 12] = [
    0b100000000000,
    0b010000000000,
    0b001000000000,
    0b000100000000,
    0b000010000000,
    0b000001000000,
    0b000000100000,
    0b000000010000,
    0b000000001000,
    0b000000000100,
    0b000000000010,
    0b000000000001,
];

pub fn run() {
    let values: Vec<u32> = parse_input();

    println!("## Day 3");
    p1(values.as_slice());
    println!();
    p2(values);
}

fn parse_input() -> Vec<u32> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).expect("fail on read input");
    let bnum = input.lines().map(
        |n| u32::from_str_radix(n, 2)
    ).collect::<Result<Vec<_>, _>>();
    return bnum.unwrap();
}

fn p1(values: &[u32]) {
    let total = values.len();
    let mut ones: [u32; 12] = [0; 12];
    for v in values {
        for i in 0..12 {
            if v & MASK[i] != 0 {
                ones[i] += 1;
            }
        }
    }
    let mut gamma: u32 = 0;
    let mut epsilon: u32 = 0;
    for i in 0..12 {
        if ones[i] > (total as u32/ 2) {
            gamma |= MASK[i];
        } else {
            epsilon |= MASK[i];
        }
    }
    println!("__Part 1:__");
    println!("{:012b} {:012b}", gamma, epsilon);
    println!("{} x {} = **{}**", gamma, epsilon, gamma*epsilon);
}

fn p2(values: Vec<u32>) {
    let mut oxygen: u32 = 0;
    let mut co2: u32 = 0;
    
    let mut d = values.clone();
    for i in 0..12 {
        let c = &d;
        if c.len() <= 1 {
            oxygen = c[0];
            break;
        }
        let (a, b): (Vec<_>, Vec<_>) = c.into_iter()
        .partition(|&&e| e & MASK[i] != 0);
        if a.len() >= b.len() {
            d = a;
        } else {
            d = b;
        }
    }

    let mut d = values.clone();
    for i in 0..12 {
        let c = &d;
        if c.len() <= 1 {
            co2 = c[0];
            break;
        }
        let (a, b): (Vec<_>, Vec<_>) = c.into_iter()
        .partition(|&&e| e & MASK[i] != 0);
        if b.len() <= a.len() {
            d = b;
        } else {
            d = a;
        }
    }

    println!("__Part 2:__");
    println!("O2 = {}\nCO2 = {}\nO2 x CO2 = **{}**", oxygen, co2, oxygen*co2);
}