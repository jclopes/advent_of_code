extern crate env_logger;

use std::{
    io::{self, Read},
};
use log::info;

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
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).expect("fail on read input");

    let values: Vec<u32> = parse_input(input);

    println!("## Day 3");
    println!("__Part 1:__");
    println!("output: {}", p1(values.as_slice()));
    println!();
    println!("__Part 2:__");
    println!("output: {}", p2(values));
}

fn parse_input(input: String) -> Vec<u32> {
    let bnum = input.lines().map(
        |n| u32::from_str_radix(n, 2)
    ).collect::<Result<Vec<_>, _>>();
    return bnum.unwrap();
}

fn p1(values: &[u32]) -> u32 {
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
    let total: u32 = values.len() as u32;
    for i in 0..12 {
        if ones[i] > (total / 2) {
            gamma |= MASK[i];
        } else {
            epsilon |= MASK[i];
        }
    }
    info!("{:012b} {:012b}", gamma, epsilon);
    info!("{} x {} = **{}**", gamma, epsilon, gamma*epsilon);
    return gamma*epsilon;
}

fn p2(values: Vec<u32>) -> u32 {
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

    info!("O2 = {}\nCO2 = {}\nO2 x CO2 = **{}**", oxygen, co2, oxygen*co2);
    return oxygen*co2;
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_part_1() {
        let input = String::from("00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010\n");
        let values = parse_input(input);

        assert_eq!(198, p1(values.as_slice()));
    }
}