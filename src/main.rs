use data_processing_rust::{get_mean, get_median, get_std}; 
use std::time::Instant;

fn main() {
    let mut data: Vec<f64> = (1..1_000_000).map(|i| i as f64).collect();

    // Measure the time for get_mean
    let start = Instant::now();
    match get_mean(&data) {
        Ok(mean) => println!("Mean: {}", mean),
        Err(e) => println!("Error calculating mean: {}", e),
    }
    let duration = start.elapsed();
    println!("Time taken by get_mean: {} microseconds", duration.as_micros());

    // Measure the time for get_median
    let start = Instant::now();
    match get_median(&mut data) {
        Ok(median) => println!("Median: {}", median),
        Err(e) => println!("Error calculating median: {}", e),
    }
    let duration = start.elapsed();
    println!("Time taken by get_median: {} microseconds", duration.as_micros());

    // Measure the time for get_std
    let start = Instant::now();
    match get_std(&data) {
        Ok(std_dev) => println!("Standard Deviation: {}", std_dev),
        Err(e) => println!("Error calculating standard deviation: {}", e),
    }
    let duration = start.elapsed();
    println!("Time taken by get_std: {} microseconds", duration.as_micros());
}
