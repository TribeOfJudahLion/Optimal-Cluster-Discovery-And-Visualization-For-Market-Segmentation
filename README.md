<br/>
<p align="center">
  <h3 align="center">Unlock Market Potential: Mastering Customer Segmentation with Optimal Cluster Analysis</h3>

  <p align="center">
    Visualize the Pulse of Your Market – Segment Smarter, Grow Faster!
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Scenario:

Imagine a marketing analytics team at an e-commerce company wants to implement a targeted marketing strategy. The company has a large customer database with various attributes, such as purchase history, website engagement metrics, and demographic information. They want to segment their customer base into distinct groups that exhibit similar behaviors and preferences to tailor marketing campaigns more effectively.

However, the challenge lies in the fact that the team is not sure how many distinct customer segments there are or how to group customers to maximize the effectiveness of their marketing efforts. They need a data-driven approach to identify these segments, understand their characteristics, and determine the optimal number of segments for targeted marketing.

### Solution Using the Provided Code:

The team decides to use KMeans clustering, an unsupervised machine learning algorithm, to solve this problem. The steps they follow are encoded in the provided Python script:

1. **Data Preparation**: The team prepares a dataset (`data_perf.txt`), where each line contains numerical attributes of a customer, such as time spent on the site, average purchase value, frequency of purchases, etc., separated by commas. This data is read from the file and stored in a NumPy array for processing.

2. **Determining Optimal Clusters**: Since the number of customer segments is unknown, the team uses the silhouette score to evaluate the quality of clusters formed for different numbers of clusters (ranging from 2 to 9). The silhouette score is a measure of how similar an object is to its own cluster compared to other clusters. The team runs KMeans clustering for each cluster count and records the silhouette scores.

   - They initialize the KMeans algorithm with `k-means++` for efficient centroid initialization, ensuring better convergence.
   - The algorithm is run 10 times (`n_init=10`) with different centroid seeds for robustness.
   - After each run, they calculate the silhouette score, which will help determine the optimal number of clusters.

3. **Visualizing Silhouette Scores**: They plot the silhouette scores against the number of clusters using a bar chart to visually determine the best number of clusters. The highest bar indicates the best number of clusters, which in this case is 5, as it has the highest silhouette score.

4. **Final Clustering**: With the optimal number of clusters determined to be 5, the team proceeds to perform final clustering using KMeans, setting `n_clusters=5`.

5. **Visualizing Clusters**: They then create a scatter plot to visualize the customer segments, using different colors to represent each of the 5 clusters. This helps in understanding the natural groupings within the customer data.

6. **Result Interpretation and Strategy Implementation**:
   - By examining the clustered data, the team can interpret each cluster's defining characteristics. For instance, Cluster 1 might represent high-value frequent shoppers, while Cluster 2 might represent occasional shoppers with low engagement.
   - Based on these insights, the marketing team can develop tailored strategies for each segment, such as sending personalized emails with recommendations to frequent shoppers or offering discounts to increase the engagement of occasional shoppers.

In conclusion, the marketing team successfully uses KMeans clustering to segment their customer base into distinct groups, providing a foundation for a more personalized and effective marketing strategy.

This code snippet demonstrates the use of the KMeans clustering algorithm from the `scikit-learn` library in Python to perform cluster analysis on a given dataset. Let's break down its functionality and logic step-by-step:

### Importing Libraries
- **NumPy**: Used for numerical operations and managing data in array format.
- **Matplotlib**: A plotting library for creating graphs and charts.
- **Scikit-learn (sklearn)**: Machine learning library. Here, it's used for the KMeans clustering algorithm and silhouette score calculation.

### Data Loading and Preprocessing
- **Reading Data**: The script reads data from a text file named 'data_perf.txt'. Each line in the file represents a data point, with values separated by commas.
- **Data Conversion**: The data from each line is split by commas, converted to floats, and added to a list `x`. This list is then converted into a NumPy array `data` for efficient manipulation.

### KMeans Clustering
- **Optimal Number of Clusters**: 
  - The script determines the optimal number of clusters ranging from 2 to 9. 
  - For each number of clusters, it initializes a KMeans model (`init='k-means++'` for smart centroid initialization, `n_init=10` for running the algorithm 10 times with different centroid seeds).
  - The model is trained (`fit`) on the data.
  - The silhouette score is calculated for each model to assess how similar an object is to its own cluster compared to other clusters. A higher silhouette score indicates better-defined clusters.
  - The silhouette scores are stored in `scores` and printed for each number of clusters.

### Plotting Silhouette Scores
- A bar graph is created to visualize the silhouette scores for different numbers of clusters, helping to select the optimal number of clusters visually.

### Final Clustering with Selected Number of Clusters
- **Final Clustering**: The script performs final clustering with 5 clusters (this number seems to be chosen arbitrarily or based on prior knowledge).
- The KMeans model is reinitialized and fitted to the data.

### Plotting Clustered Data
- A scatter plot is created to visualize the data points, colored differently for each of the 5 clusters.
- The plot is labeled and a legend is added for clarity.

### Display Plots
- `plt.show()` displays all the plots generated.

### Summary
- This script is a typical example of unsupervised learning using KMeans clustering. It demonstrates data loading, preprocessing, model fitting, evaluation using silhouette scores, and visualization of the results through plots. The primary goal here is to identify natural groupings in the data based on their features.

The output results consist of two parts: textual console output indicating silhouette scores for different numbers of clusters, and two graphical plots visualizing these scores and the resulting clusters.

### Console Output Explanation:
The printed output on the console provides silhouette scores for the number of clusters ranging from 2 to 9. The silhouette score measures how similar an object is to its own cluster (cohesion) compared to other clusters (separation). A high silhouette score indicates that the object is well matched to its own cluster and poorly matched to neighboring clusters. Here are the silhouette scores for the given number of clusters:
- 2 Clusters: Score = 0.5290
- 3 Clusters: Score = 0.5552
- 4 Clusters: Score = 0.5833
- 5 Clusters: Score = 0.6583 (highest score, indicating the best cluster separation for this number)
- 6 Clusters: Score = 0.5992
- 7 Clusters: Score = 0.5195
- 8 Clusters: Score = 0.4597
- 9 Clusters: Score = 0.4022

### Silhouette Score vs Number of Clusters Plot:
The first plot is a bar chart that visually represents the silhouette scores that were output to the console. The x-axis represents the number of clusters and the y-axis represents the silhouette score. The bar for 5 clusters is the tallest, indicating it has the highest silhouette score among the evaluated range. This suggests that dividing the dataset into 5 clusters results in the most distinct and well-separated clusters according to the silhouette metric.

### Clustered Data Plot:
The second plot shows the actual clustering of the dataset when divided into 5 groups (as 5 had the highest silhouette score). The plot is a scatter plot with the x-axis and y-axis representing two features of the dataset. Each point represents a data sample, and points are colored based on the cluster they belong to, as determined by the KMeans algorithm. There are 5 different colors, corresponding to the 5 clusters. This visual representation allows us to see how the algorithm has grouped the data into clusters based on the similarity of their features.

In summary, the output indicates that for this particular dataset, creating 5 clusters results in the most distinct groups according to the silhouette score, and the scatter plot provides a visual confirmation of how these clusters are distributed in the feature space.

## Built With

This project implements a KMeans clustering solution, utilizing a set of powerful, open-source software libraries. The main components are:

- **[NumPy](https://numpy.org/)** - A fundamental package for scientific computing with Python. It provides a high-performance multidimensional array object and tools for working with these arrays. It's used here for efficient data storage and manipulation, transforming the input data into an array format suitable for machine learning algorithms.
  
- **[Matplotlib](https://matplotlib.org/)** - A comprehensive library for creating static, animated, and interactive visualizations in Python. In this project, Matplotlib is used to generate plots that provide visual insights into the data and the results of the clustering analysis. It's responsible for creating the silhouette score plot and the scatter plot of clustered data, which are crucial for determining the optimal number of clusters and for visualizing the distribution of data points within each cluster.

- **[scikit-learn (sklearn)](https://scikit-learn.org/stable/)** - A machine learning library for Python. It features various classification, regression, and clustering algorithms, including KMeans, which is used in this project to perform the clustering operation. The library also provides tools for model fitting, data preprocessing, model selection, and evaluation. The metrics module from scikit-learn is utilized here to compute the silhouette scores, which measure how well-separated the clusters are.

- **Python Standard Library** - The built-in `open` function is used for file operations, reading the input data from a text file (`data_perf.txt`). This demonstrates the integration of Python's core capabilities with external libraries to facilitate the entire data analysis workflow.

The project is structured to ensure that it's modular, scalable, and maintainable. The code can be adapted to different datasets or clustering problems by simply changing the input file and possibly adjusting the range of cluster numbers to test. This makes it an excellent template for a wide range of clustering applications in areas such as market segmentation, social network analysis, urban planning, and more.

To recreate this project's environment or contribute to its development, you will need to install the aforementioned libraries. Each library's installation can be typically managed through Python's package manager pip, as follows:

```shell
pip install numpy matplotlib scikit-learn
```

Please ensure you are using a compatible version of Python, preferably Python 3.x, as this is the version with which these libraries are most commonly used and tested.

## Getting Started

This section will guide you through setting up your local machine for running and contributing to this KMeans clustering project.

#### Prerequisites

- **Python**: You should have Python installed on your machine. The recommended version is Python 3.8 or higher, which you can download and install from [python.org](https://www.python.org/).
  
- **Pip**: Ensure that Python's package manager pip is installed. It usually comes with Python, but you can check the installation by running `pip --version` in your command line.

- **Virtual Environment (Optional but recommended)**: It is good practice to use a virtual environment to manage dependencies for the project. You can create one using Python's built-in `venv` module or with `virtualenv`.

#### Installation

1. **Clone the repository**:
   ```shell
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Set up a virtual environment** (optional):
   - For `venv`:
     ```shell
     python -m venv venv
     ```
     - Activate it with:
       - Windows: `venv\Scripts\activate`
       - Unix or MacOS: `source venv/bin/activate`
   - For `virtualenv`:
     ```shell
     virtualenv venv
     ```
     - Activate it as described above.

3. **Install required packages**:
   ```shell
   pip install numpy matplotlib scikit-learn
   ```

#### Running the code

1. **Prepare your dataset**: Make sure you have a dataset file named `data_perf.txt` in the project directory. This file should contain numerical data in CSV format (comma-separated values), where each line represents a data point.

2. **Run the script**: You can run the clustering script with the following command:
   ```shell
   python kmeans_clustering.py
   ```
   Replace `kmeans_clustering.py` with the actual name of your script if different.

3. **View Results**: The script will print the silhouette scores for different cluster counts to the console and show two plots:
   - A bar chart of silhouette scores vs. the number of clusters.
   - A scatter plot of the data points colored by their assigned cluster.

#### Understanding the Output

- **Console Output**: Look for the printout of silhouette scores to understand how well the data is clustered for each number of clusters tested.
- **Plots**: Examine the plots that pop up to visually inspect the clustering results.

#### Troubleshooting

- If the plots do not display, ensure you have a GUI backend for Matplotlib installed and configured.
- If you encounter any package-related errors, double-check the versions of the installed packages and consult the official documentation for compatibility information.

By following these steps, you should be able to get the KMeans clustering project running on your local machine. For contributing to the project, check out the `CONTRIBUTING.md` file in the repository for guidelines on how to make pull requests, report bugs, and request features.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/TribeOfJudahLion/Optimal Cluster Discovery and Visualization for Market Segmentation/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/TribeOfJudahLion/Optimal Cluster Discovery and Visualization for Market Segmentation/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/TribeOfJudahLion/Optimal Cluster Discovery and Visualization for Market Segmentation/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion) - **

## Acknowledgements

* []()
* []()
* []()
