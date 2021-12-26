extern crate env_logger;
use log::error;
use std::env;

mod d03;

fn main() {
    env_logger::init();
    if let Some(arg) = env::args().nth(1) {
        match arg.as_str() {
            "3" => d03::run(),
            _ => error!("not implemented or invalid argument: {}", arg),
        };
    } else {
        error!("missing day argument");
    }
}