#!/usr/bin/env python3

from openai import OpenAI
from string import Template

client = OpenAI()

PROMPT = Template(
    "$prompt\n\n<CBMC DOCUMENTATION>\n$cbmc_docs\n</CBMC DOCUMENTATION>\n\n<C SOURCE FILE>\n$code\n</C SOURCE FILE>\n\n<C HEADER FILE>\n$header\n</C HEADER FILE>\n\n<EXAMPLE>\n$example_spec\n</EXAMPLE>"
)

with (
    open("./system-prompt.txt", mode="r") as f0,
    open("./prompt.txt", mode="r") as f1,
    open("./contracts-requires-ensures.html", mode="r") as f2,
    open("./crypto.c", mode="r") as f3,
    open("./crypto.h", mode="r") as f4,
    open("./example.txt", mode="r") as f5,
):
    system_prompt = f0.read()
    user_prompt = f1.read()
    cbmc_spec_document = f2.read()
    crypto_function = f3.read()
    header_file = f4.read()
    example_spec = f5.read()

user_prompt = PROMPT.safe_substitute(
        prompt=user_prompt,
        cbmc_docs=cbmc_spec_document,
        code=crypto_function,
        header=header_file,
        example_spec=example_spec)

print(user_prompt)

response = client.responses.create(
    model="gpt-4o-2024-05-13",
    instructions=system_prompt,
    input=user_prompt,
    temperature=0,
)

print(response.output_text)
