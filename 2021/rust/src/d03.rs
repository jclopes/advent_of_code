// use std::{
//     io::{self, Read},
// };

use std::io;
use std::io::Read;

pub fn p1() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).expect("fail on read input");
    let bnum = input.lines().map(
        |n| i32::from_str_radix(n, 2)
    ).collect::<Result<Vec<_>, _>>();
    println!("{:?}", bnum);
}