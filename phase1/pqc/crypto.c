#include "crypto.h"

uint16_t mod3329(uint16_t a, uint16_t b)
{
  int32_t r1 = (int32_t)a * (int32_t)b;
  int64_t r2 = r1 * magic;
  int32_t r3 = (int32_t)(r2 / c);
  int32_t r4 = r3 * Q;
  int32_t r = r1 - r4;
  return (uint16_t)r;
}

#define QINV -3327  // q^-1 mod 2^16

// This code from the Kyber reference implementation.
int16_t mr1(int32_t a)
{
  int16_t t;

  t = (int16_t)a * QINV; 
  t = (a - (int32_t)t * Q) >> 16;
  return t;
}

void mod3329_harness()
{
  uint16_t x, y;
  uint16_t r;
  r = mod3329(x, y);
}

void mr1_harness()
{
  int32_t a;
  int16_t r;
  r = mr1(a);
}