import os
import argparse
import tombo.globals as g
from tombo.tombo import tombo
from tombo.plotting import create_directories, generate_plots, view_plot

def tombo2(parser, args):
    tombo()

def generate_plots2(parser, args):
    if not os.path.isdir(args.data_folder):
        parser.exit("Invalid data folder path")

    create_directories(g.plot_folder)
    generate_plots(args.data_folder)

def view_plot2(parser, args):
    if not os.path.isfile(args.data_file):
        parser.exit("Invalid data file path")

    view_plot(args.data_file)

def sim_and_plot(parser, args):
    tombo()
    create_directories(g.plot_folder)
    generate_plots(g.data_folder)

def init_parsers():
    global_parser = argparse.ArgumentParser(
        prog='tombo',
        description="Simulate and generate plots for a 3D flapping wings simulation"
    )
    subparsers = global_parser.add_subparsers(title='subcommands')

    sim_parser = subparsers.add_parser(
        'sim',
        help='run simulation (configurable with config.toml)'
    )
    sim_parser.set_defaults(func=tombo2)

    plot_parser = subparsers.add_parser('plot', help='generate plots')
    plot_parser.add_argument(
        'data_folder',
        nargs='?',
        default=g.data_folder,
        help="path to folder containing data generated by the simulation"
    )
    plot_parser.set_defaults(func=generate_plots2)

    view_parser = subparsers.add_parser(
        'view',
        help='open plot in interactive viewer'
    )
    view_parser.add_argument('data_file', help='path to data file to plot')
    view_parser.set_defaults(func=view_plot2)

    simplot_parser = subparsers.add_parser(
        'simplot',
        help="run simulation and generate plots (configurable with config.toml)"
    )
    simplot_parser.set_defaults(func=sim_and_plot)

    return global_parser

def main():
    parser = init_parsers()
    args = parser.parse_args()
    args.func(parser, args)

if __name__ == '__main__':
    main()
