"""
The command line interface to update route53 PTR records, and associate to vpc.
"""
"""
The command line interface to cfn_rules.
"""
import sys
import logging
import click
from r53_ptr_vpc_associator.Associator import Associator

LOGGER = logging.getLogger()

@click.group()
@click.version_option(version='0.5.4')
def cli():
    pass


@cli.command()
@click.option('--profile-name', '-n', help='profile name', required=True)
@click.option('--debug/--no-debug', help='debug', default=False)
def zone_list(profile_name, debug):
    """
    List vpcs for hosted zones
    """
    if debug:
        LOGGER.setLevel(logging.DEBUG)

    if debug:
        LOGGER.setLevel(logging.DEBUG)
        logging.debug('profile_name: '+str(profile_name))

    if not profile_name:
        print('Must have profile name.  Run \'associator list --help\' to see required parameters')
        sys.exit(1)

    associator = Associator(
        profile_name=profile_name,
        debug=debug
    )

    print(associator.list_hosted_zones(pretty=True))


@cli.command()
@click.option('--profile-name', '-n', help='profile name', required=True)
@click.option('--vpc-id', '-n', help='vpc id to associate to hosted zones', required=True)
@click.option('--vpc-region', '-n', help='vpc region to associate to hosted zones', required=True)
@click.option('--debug/--no-debug', help='debug', default=False)
def associate(profile_name, vpc_id, vpc_region, debug):
    """
    Associated hosted zones to vpc
    """
    if debug:
        LOGGER.setLevel(logging.DEBUG)

    if debug:
        LOGGER.setLevel(logging.DEBUG)
        logging.debug("profile_name: %s", profile_name)
        logging.debug("vpc_id: %s", vpc_id)
        logging.debug("vpc_region: %s", vpc_region)

    if not profile_name:
        print('Must have profile name.  Run \'associator associate'
              ' --help\' to see required parameters')
        sys.exit(1)

    if not vpc_id:
        print('Must have vpc_id.  Run \'associator associate'
              ' --help\' to see required parameters')
        sys.exit(1)

    if not vpc_region:
        print('Must have vpc_region.  Run \'associator associate'
              ' --help\' to see required parameters')
        sys.exit(1)

    associator = Associator(
        profile_name=profile_name,
        debug=debug,
        vpc_id=vpc_id,
        vpc_region=vpc_region
    )

    print(associator.associate_zones_to_vpc(pretty=True))
