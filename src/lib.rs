use std::error::Error;

pub fn get_mean(x: &Vec<f64>) -> Result<f64, Box<dyn Error>> {
    if x.is_empty() {
        return Err("Cannot compute mean of an empty vector.".into());
    }
    let sum: f64 = x.iter().sum();
    Ok(sum / x.len() as f64)
}

pub fn get_median(x: &mut Vec<f64>) -> Result<f64, Box<dyn Error>> {
    if x.is_empty() {
        return Err("Cannot compute median of an empty vector.".into());
    }
    x.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mid = x.len() / 2;
    if x.len() % 2 == 0 {
        Ok((x[mid - 1] + x[mid]) / 2.0)
    } else {
        Ok(x[mid])
    }
}

pub fn get_std(x: &Vec<f64>) -> Result<f64, Box<dyn Error>> {
    if x.len() < 2 {
        return Err("Need at least two data points to compute standard deviation.".into());
    }
    let mean = get_mean(x)?;
    let variance: f64 = x.iter().map(|value| (value - mean).powi(2)).sum::<f64>() / (x.len() - 1) as f64;
    Ok(variance.sqrt())
}
