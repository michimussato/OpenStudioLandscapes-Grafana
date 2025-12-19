import textwrap

import snakemd


def readme_feature(
    doc: snakemd.Document,
    main_header: str,
) -> snakemd.Document:

    # Some Specific information

    doc.add_heading(
        text=main_header,
        level=1,
    )

    doc.add_quote(
        text=textwrap.dedent(
            """\
            [!CAUTION]

            Starting with Grafana release `12.4.0`,
            the `grafana/grafana-oss` Docker Hub
            repository will no longer be updated.
            Instead, we encourage you to use
            the `grafana/grafana` Docker Hub
            repository. These two repositories
            have the same Grafana OSS docker images.

            ([Source](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/))\
            """
        )
    )

    # Logo

    doc.add_paragraph(
        snakemd.Inline(
            text=textwrap.dedent(
                """\
                Logo Grafana\
                """
            ),
            image="https://grafana.com/media/products/cloud/grafana/grafana-product-logo.svg",
            link="https://grafana.com/grafana/",
        ).__str__()
    )

    doc.add_paragraph(
        text=textwrap.dedent(
            """\
            Grafana is written and maintained by Grafana Labs.\
            """
        )
    )

    # Logo

    # doc.add_paragraph(
    #     snakemd.Inline(
    #         text=textwrap.dedent(
    #             """
    #             Logo Ynput
    #             """
    #         ),
    #         image={
    #             "Ynput": "https://ynput.io/wp-content/uploads/2022/09/ynput-logo-small-bg.svg",
    #         }["Ynput"],
    #         link="https://ynput.io",
    #     ).__str__()
    # )

    doc.add_paragraph(
        text=textwrap.dedent(
            """\
            Grafana Labs offers different versions of Grafana:\
            """
        )
    )

    doc.add_unordered_list(
        [
            "OSS",
            "Enterprise",
        ]
    )

    doc.add_paragraph(
        text=textwrap.dedent(
            """\
            `OpenStudioLandscapes-Grafana` is based on the [OSS](https://ynput.io/ayon/pricing/)
            version provided by their own Docker image:\
            """
        )
    )

    doc.add_unordered_list(
        [
            "[`docker.io/grafana/grafana`](https://hub.docker.com/r/grafana/grafana)",
        ]
    )

    doc.add_heading(
        text="Official Documentation",
        level=2,
    )

    doc.add_unordered_list(
        [
            "[Setup](https://grafana.com/docs/grafana/latest/setup-grafana/)",
            "[Install](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)",
            "[Configure a Docker Image](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/)",
            "[Administration](https://grafana.com/docs/grafana/latest/administration/)",
        ]
    )

    doc.add_heading(
        text="Grafana Alloy",
        level=3,
    )

    doc.add_paragraph(
        text=textwrap.dedent(
            """\
            Alloy can collect, process, 
            and export telemetry signals to 
            scale and future-proof your observability approach.
            More info:\
            """
        )
    )

    doc.add_unordered_list(
        [
            "[https://grafana.com/docs/alloy/latest/](https://grafana.com/docs/alloy/latest/)",
        ]
    )

    doc.add_heading(
        text="Alloy Scenarios",
        level=4,
    )

    doc.add_paragraph(
        text=textwrap.dedent(
            """\
            This repository contains scenarios that 
            demonstrate how to use Grafana Alloy to 
            monitor various data sources. 
            Each scenario is a self-contained example 
            which will include an LGMT stack 
            (Loki, Grafana, Metrics, Tempo) and an 
            Alloy configuration file.\
            """
        )
    )

    doc.add_unordered_list(
        [
            "[https://github.com/grafana/alloy-scenarios/](https://github.com/grafana/alloy-scenarios/)",
        ]
    )

    doc.add_heading(
        text="Configure Grafana",
        level=2,
    )

    doc.add_heading(
        text="Default Paths",
        level=3,
    )

    doc.add_unordered_list(
        [
            "[Default paths](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/#default-paths)",
        ]
    )

    doc.add_heading(
        text="`defaults.ini`",
        level=3,
    )

    doc.add_paragraph(
        text=textwrap.dedent(
            """\
            As it turned out, the contents of the `defaults.ini` file are
            tied to the Grafana version. A mismatch can lead to a non-functional
            container (see [issue](https://github.com/michimussato/OpenStudioLandscapes-Grafana/issues/7)).
            Hence, the `defaults.ini` file can't be managed by an OpenStudioLandscapes Dagster asset
            without compromising cross-version compatibility.
            The main entry point for Grafana configuration is therefore the [`grafana.ini`](#grafanaini) file
            (exclusively).
            """
        )
    )

    doc.add_heading(
        text="`grafana.ini`",
        level=3,
    )

    doc.add_unordered_list(
        [
            "[Configure Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/)",
        ]
    )

    # doc.add_heading(
    #     text="A",
    #     level=3,
    # )
    #
    # doc.add_unordered_list(
    #     [
    #         "[REST API Docs](https://docs.ayon.dev/api)",
    #         "[GraphQL API Explorer](https://playground.ayon.app/explorer)",
    #         "[Python API Docs](https://docs.ayon.dev/ayon-python-api)",
    #         "[C++ API Docs](https://docs.ayon.dev/ayon-cpp-api)",
    #         "[USD Resolver Docs](https://docs.ayon.dev/ayon-usd-resolver)",
    #         "[Frontend React Components](https://components.ayon.dev)",
    #     ]
    # )

    return doc


if __name__ == "__main__":
    pass
