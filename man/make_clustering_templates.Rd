% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/cluster_templates.R
\name{make_clustering_templates}
\alias{make_clustering_templates}
\title{Make Clustering Templates}
\usage{
make_clustering_templates(
  template_dir,
  template_images_dir,
  writer_indices,
  max_edges = 30,
  centers_seed,
  graphs_seed,
  K = 40,
  num_dist_cores = 1,
  num_path_cuts = 8,
  max_iters = 1,
  gamma = 3,
  num_graphs = "All"
)
}
\arguments{
\item{template_dir}{Main directory that will store template files}

\item{template_images_dir}{A directory containing template training images}

\item{writer_indices}{A vector of the starting and ending location of the
writer ID in the file name.}

\item{max_edges}{Maximum number of edges allowed in input graphs. Graphs with
more than the maximum number will be ignored.}

\item{centers_seed}{Integer seed for the random number generator when
selecting starting cluster centers.}

\item{graphs_seed}{Integer seed for the random number generator when
selecting graphs. If \code{num_graphs = 'All'} then \code{graphs_seed} won't be used}

\item{K}{Integer number of clusters}

\item{num_dist_cores}{Integer number of cores to use for the distance
calculations in the K-means algorithm. Each iteration of the K-means
algorithm calculates the distance between each input graph and each cluster
center.}

\item{num_path_cuts}{Integer number of sections to cut each graph into for
shape comparison}

\item{max_iters}{Maximum number of iterations to allow the K-means algorithm
to run}

\item{gamma}{Parameter for outliers}

\item{num_graphs}{Number of graphs to use to create the cluster template.
\code{All} uses all available graphs. An integer uses a random sample of graphs.}
}
\value{
List containing the cluster template
}
\description{
\code{make_clustering_templates()} applies a K-means clustering algorithm to the
input handwriting samples pre-processed with \code{\link[=process_batch_dir]{process_batch_dir()}} and saved
in the input folder \verb{template_dir > data > template_graphs}. The K-means
algorithm sorts the graphs in the input handwriting samples into groups, or
\emph{clusters}, of similar graphs.
}
\examples{
\dontrun{
main_dir <- "path/to/folder"
template_images_dir <- system.file("extdata/example_images/template_training_images",
  package = "handwriter"
)
template_list <- make_clustering_templates(
  template_dir = main_dir,
  template_images_dir = template_images_dir,
  writer_indices = c(2, 5),
  K = 10,
  num_dist_cores = 2,
  max_iters = 3,
  num_graphs = 1000,
  centers_seed = 100,
  graphs_seed = 200
)
}

}
