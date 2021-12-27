extern crate env_logger;

use std::{
    io::{self, Read},
};
use log::info;

pub fn run() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).expect("fail on read input");

    let (values, size) = parse_input(input);

    println!("## Day 3");
    println!("__Part 1:__");
    println!("output: {}", p1(values.as_slice(), size));
    println!();
    println!("__Part 2:__");
    println!("output: {}", p2(values, size));
}

fn parse_input(input: String) -> (Vec<u32>, usize) {
    let bnum = input.lines().map(
        |n| u32::from_str_radix(n, 2)
    ).collect::<Result<Vec<_>, _>>();
    let size = input.lines().next().unwrap().len();
    return (bnum.unwrap(), size);
}

fn mask(len: usize) -> Vec<u32> {
    let mut res = Vec::new();
    
    for i in (0..len).rev() {
        res.push(1<<i);
    }
    return res;
}

fn p1(values: &[u32], size: usize) -> u32 {
    let mask_vec = mask(size);
    let mut ones: [u32; 12] = [0; 12];
    for v in values {
        for i in 0..size {
            if v & mask_vec[i] != 0 {
                ones[i] += 1;
            }
        }
    }
    let mut gamma: u32 = 0;
    let mut epsilon: u32 = 0;
    let total: u32 = values.len() as u32;
    for i in 0..size {
        if ones[i] > (total / 2) {
            gamma |= mask_vec[i];
        } else {
            epsilon |= mask_vec[i];
        }
    }
    info!("{:012b} {:012b}", gamma, epsilon);
    info!("{} x {} = **{}**", gamma, epsilon, gamma*epsilon);
    return gamma*epsilon;
}

fn p2(values: Vec<u32>, size: usize) -> u32 {
    let mut oxygen: u32 = 0;
    let mut co2: u32 = 0;
    let mask_vec = mask(size);
    
    let mut v = values.clone();
    for i in 0..size {
        if v.len() <= 1 {
            oxygen = v[0];
            break;
        }
        let (a, b): (Vec<_>, Vec<_>) = v.into_iter()
        .partition(|&e| e & mask_vec[i] != 0);
        if a.len() >= b.len() {
            v = a;
        } else {
            v = b;
        }
    }

    let mut v = values.clone();
    for i in 0..size {
        if v.len() <= 1 {
            co2 = v[0];
            break;
        }
        let (a, b): (Vec<_>, Vec<_>) = v.into_iter()
        .partition(|&e| e & mask_vec[i] != 0);
        if b.len() <= a.len() {
            v = b;
        } else {
            v = a;
        }
    }

    info!("O2 = {}\nCO2 = {}\nO2 x CO2 = **{}**", oxygen, co2, oxygen*co2);
    return oxygen*co2;
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_parse_input() {
        let expected = vec![
            0b00100,
            0b11110,
            0b10110,
            0b10111,
            0b10101,
            0b01111,
            0b00111,
            0b11100,
            0b10000,
            0b11001,
            0b00010,
            0b01010];
        let input = String::from("00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010\n");
        let (values, size) = parse_input(input);
        assert_eq!(5, size);
        assert_eq!(expected, values)
    }

    #[test]
    fn test_p1() {
        let input = String::from("00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010\n");
        let (values, size) = parse_input(input);

        assert_eq!(198, p1(values.as_slice(), size));
    }

    #[test]
    fn test_mask() {
        let expected12: Vec<u32> = vec![
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
            0b000000000001];

        let expected06: Vec<u32> = vec![
            0b100000,
            0b010000,
            0b001000,
            0b000100,
            0b000010,
            0b000001];
    
        assert_eq!(expected12, mask(12));
        assert_eq!(expected06, mask(6));
    }
}